import { Tooltip, Button, Modal, ToastContainer, useToast, Card, Divider, Accordion, AccordionItem } from 'sketchbook-ui';
import { Creator } from './Creator';
import { useState } from 'react';

export function App() {
    const { toasts, showToast, dismissToast } = useToast();
    const [openModal, setOpenModal] = useState(false);
    const [qry, setQry] = useState<queryfmt>(()=>getQry().qry);
    const [urlMode, setUrlMode] = useState<'srch'|'hash'>(()=>getQry().mode);
    function getQry(): {mode: 'srch'|'hash', qry: queryfmt} {
        let srch = window.location.search.substring(1);
        let hash = window.location.hash.substring(1);
        if(srch){
            try{
                let parsed = JSON.parse(decodeURIComponent(srch));
                return {mode: 'srch', qry: {
                    title: parsed.title || 'Untitled',
                    desc: parsed.desc || '',
                    links: parsed.links.map((l:any) => ({ name: l.name || 'Link', url: l.url || '' })) || [],
                    tgb: parsed.tgb || false,
                }}
            }catch(e){
                showToast('Parse SearchParams JSON: Invalid JSON', 'error');
            };
        };
        if(hash){
            try{
                let parsed = JSON.parse(new TextDecoder().decode(new Uint8Array(atob(hash).split('').map(c => c.charCodeAt(0)))));
                return {mode: 'hash', qry: {
                    title: parsed.title || 'Untitled',
                    desc: parsed.desc || '',
                    links: parsed.links.map((l:any) => ({ name: l.name || 'Link', url: l.url || '' })) || [],
                    tgb: parsed.tgb || false,
                }}
            }catch(e){
                showToast('Parse Hash: Invalid Format', 'error');
            };
        };
        return {mode: 'srch', qry: {
            title: 'Selinkt',
            desc: 'Create your link selector via the button!',
            links: [],
            tgb: false,
        }}
    };

    return (
        <div className='flex'>
            <div className='fixed top-4 right-4'>
                <Tooltip content="Create!" placement="left">
                    <Button iconOnly size="sm" typography={{fontSize: '3rem'}}
                        onClick={() => setOpenModal(true)}
                    >+</Button>
                </Tooltip>
                <Modal 
                    isOpen={openModal} 
                    onClose={() => setOpenModal(false)}
                    title="Create a Selinkt"
                >
                    <Creator qry={qry} setQry={setQry} um={urlMode} setUm={setUrlMode} />
                </Modal>
            </div>
            <ToastContainer
                toasts={toasts}
                onDismiss={dismissToast}
                position="top-right"
            />
            <Card className='mt-25 ml-5 mr-5 mb-10 flex flex-col'>
                <h1 className='text-6xl'>{qry.title}</h1>
                <p className='text-2xl whitespace-pre'>{qry.desc}</p>
                <Divider variant='zigzag' />
                <Accordion className='w-full max-w-114514!'>
                    {qry.links.map((l, i) => (
                        <AccordionItem key={i} title={l.name} defaultOpen>
                            <a href={l.url} target={qry.tgb ? '_blank' : '_self'} className='text-center text-orange-600 text-2xl underline block break-all'>{l.url}</a>
                        </AccordionItem>
                    ))}
                </Accordion>
            </Card>
        </div>
    );
};