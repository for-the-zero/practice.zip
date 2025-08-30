const { app, Tray, Menu, nativeImage, dialog, clipboard, globalShortcut, shell } = require('electron');
const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');
const { screen } = require('@nut-tree-fork/nut-js');

const configPath = app.isPackaged
    ? path.join(path.dirname(app.getPath('exe')), 'config.json')
    : path.join(__dirname, 'config.json');
function loadConfig() {
    try {
        if (fs.existsSync(configPath)) {
            const rawData = fs.readFileSync(configPath, 'utf-8');
            return JSON.parse(rawData);
        };
    } catch (error) {
        console.error("Error reading or parsing config.json:", error);
        dialog.showErrorBox("Configuration Error", "Failed to read or parse config.json. Using default settings.");
    };
    return {
        ss_save_path: path.join(app.getPath('documents'), 'SnapShotScreen')
    };
};
let config = loadConfig();
if (!fs.existsSync(configPath)) {
    try {
        fs.writeFileSync(configPath, JSON.stringify(config, null, 2), 'utf-8');
    } catch (error) {
        console.error("Failed to write initial config file:", error);
    }
};


if(app.isPackaged){
    app.setLoginItemSettings({ openAtLogin: true });
};

function restart_as_admin() {
    // In a packaged app, elevate.exe is in the resources folder.
    const elevatePath = app.isPackaged 
        ? path.join(process.resourcesPath, 'elevate.exe')
        : path.join(__dirname, 'elevate.exe'); // Fallback for development

    const exePath = process.execPath;
    console.log('elevate.exe path:', elevatePath);
    console.log('Target EXE path:', exePath);
    const child = spawn(elevatePath, [exePath], {
        detached: true,
        stdio: 'ignore',
    });
    child.unref();
    app.quit();
};

let tray = null;
app.whenReady().then(() => {
    var screenshot_mode = 1;
    const ss_mode_change = (mode) => {
        screenshot_mode = mode;
        switch (mode) {
            case 0:
                del_ssmode1();
                del_ssmode2();
                break;
            case 1:
                reg_ssmode1();
                del_ssmode2();
                break;
            case 2:
                del_ssmode1();
                reg_ssmode2();
                break;
            default:
                break;
        };
    };
    ss_mode_change(1);
    tray = new Tray(path.join(__dirname, 'icon.png'));
    const contextMenu = Menu.buildFromTemplate([
        { label: '截图模式', type: 'submenu', submenu: [
            { label: '关闭', type: 'radio', checked: screenshot_mode === 0, click: () => { ss_mode_change(0) } },
            { label: '按键检测', type: 'radio', checked: screenshot_mode === 1, click: () => { ss_mode_change(1) } },
            { label: '剪贴板识别', type: 'radio', checked: screenshot_mode === 2, click: () => { ss_mode_change(2) } },
        ] },

        { label: '管理员身份重启', type: 'normal', click: () => { restart_as_admin() } },
        { label: '打开配置文件', type: 'normal', click: ()=>{ open_config(); } },
        { label: '退出', type: 'normal', click: () => { app.quit() } }
    ]);
    tray.setContextMenu(contextMenu);
});
if(fs.existsSync(config.ss_save_path) === false){
    fs.mkdirSync(config.ss_save_path, { recursive: true });
};
function del_ssmode1(){
    globalShortcut.unregister('PrintScreen');
};
function reg_ssmode1(){
    globalShortcut.register('PrintScreen',async()=>{
        await screen.capture(
            fileName=`screenshot_${Date.now()}`,
            fileFormat='.png',
            filePath=config.ss_save_path
        );
        //console.log('Screenshot saved');
    });
};

var ssm2_interval = null;
var ssm2_last_hash = null;
function del_ssmode2(){
    if(ssm2_interval){
        clearInterval(ssm2_interval);
        ssm2_interval = null;
    };
};
function reg_ssmode2(){
    ssm2_interval = setInterval(()=>{
        const image = clipboard.readImage();
        let hash = image.toDataURL();
        if( image.isEmpty() || hash === ssm2_last_hash ){return;};
        ssm2_last_hash = hash;
        fs.writeFile(
            path.join(config.ss_save_path, `screenshot_${Date.now()}.png`), 
            image.toPNG(), 
            (err) => {
                if(err){
                    console.error(err);
                    dialog.showErrorBox('错误', err.message);
                }else{
                    //console.log('Screenshot saved');
                };
            }
        );
    },1000);
};

function open_config(){
    shell.openPath(configPath).catch(err => {
        console.error("Failed to open config file:", err);
        dialog.showErrorBox("Error", "Could not open the configuration file.");
    });
};
