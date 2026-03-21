import dearpygui.dearpygui as dpg
import psutil
import time

dpg.create_context()
dpg.create_viewport(title='perfqk', width=600, height=600)

cpudatax = []
cpudatay = []
memdatax = []
memdatay = []

with dpg.window(label="perfqk", tag='Pwin'):
    open_cpu = dpg.add_checkbox(label="Start")
    with dpg.plot(height=-1, width=-1, no_child=True, no_menus=True, no_box_select=True, pan_button=-1):
        dpg.add_plot_axis(dpg.mvXAxis)
        dpg.set_axis_limits(dpg.last_item(), 0, 150)
        dpg.add_plot_axis(dpg.mvYAxis, tag="axis_y")
        dpg.set_axis_limits(dpg.last_item(), 0, 100)
        dpg.add_line_series(cpudatax,cpudatay,tag="cpu_line",parent="axis_y")
        dpg.add_line_series(cpudatax,cpudatay,tag="mem_line",parent="axis_y")

        


        
        

dpg.setup_dearpygui()
dpg.show_viewport()

dpg.set_primary_window('Pwin',True)

cpulist = []
memlist = []
times = list(range(150))
while dpg.is_dearpygui_running():

    if dpg.get_value(open_cpu):
        if len(cpulist) == 150:
            cpulist.pop(0)
        cpulist.append(psutil.cpu_percent())
        true_cpulist = [0] * (150 - len(cpulist)) + cpulist
        dpg.set_value('cpu_line', [times,true_cpulist])
        if len(memlist) == 150:
            memlist.pop(0)
        memlist.append(psutil.virtual_memory().percent)
        true_memlist = [0] * (150 - len(memlist)) + memlist
        dpg.set_value('mem_line', [times,true_memlist])

    time.sleep(0.2)

    dpg.render_dearpygui_frame()


dpg.destroy_context()