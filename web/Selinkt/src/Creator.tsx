import { Button, Input, Textarea, Select, Switch } from "sketchbook-ui";
import { use, useEffect } from "react";
export function Creator({ qry, setQry, um, setUm }: { qry: queryfmt, setQry: React.Dispatch<React.SetStateAction<queryfmt>>, um: 'srch'|'hash', setUm: React.Dispatch<React.SetStateAction<'srch'|'hash'>> }) {

    useEffect(()=>{
        let json = JSON.stringify(qry);
        if(um === 'srch'){
            window.history.replaceState(null, '', window.location.pathname + '?' + json);
        }else{
            window.history.replaceState(null, '', window.location.pathname + '#' + btoa(new TextEncoder().encode(json).reduce((s, b) => s + String.fromCharCode(b), "")));
        };
    }, [qry, um]);


    return (
        <div className="flex flex-col p-3 w-full">
            <label className="ml-2 mb-2">Mode</label>
            <Select
                options={[
                    {value: 'srch', label: 'SearchParams'},
                    {value: 'hash', label: 'Hash'}
                ]}
                defaultValue={um}
                onChange={setUm as (value: string) => void}
            />
            <Switch className="mb-3" label="Open In New Tab?" checked={qry.tgb} onChange={(e) => setQry((prev)=>({...prev, tgb: e.target.checked}))} />
            <Input
                label="Selinkt Title"
                value={qry.title}
                onChange={(e) => setQry((prev)=>({...prev, title: e.target.value}))}
            />
            <div className="flex flex-col">
            </div>
            <Textarea
                label="Description"
                value={qry.desc}
                onChange={(e) => setQry((prev)=>({...prev, desc: e.target.value}))}
            />
            <label className="ml-2 mb-2"><b>Links</b></label>
            <div className="overflow-x-auto overflow-y-hidden flex flex-col max-w-full pt-1 pb-1">
                {qry.links.map((link, i) => (
                    <div key={i} className="flex flex-row">
                        <Button className="translate-y-4 ml-1!" iconOnly size="sm" onClick={()=>{setQry((prev)=>({...prev, links: prev.links.filter((_, idx) => idx !== i)}))}} typography={{fontSize: '3rem'}}>×</Button>
                        <Input label="Name" className="w-30! min-w-auto!" value={link.name} onChange={(e)=>{setQry((prev)=>({...prev, links: prev.links.map((l, idx) => idx === i ? {...l, name: e.target.value} : l)}))}} />
                        <Input label="Link" value={link.url} onChange={(e)=>{setQry((prev)=>({...prev, links: prev.links.map((l, idx) => idx === i ? {...l, url: e.target.value} : l)}))}} />
                    </div>
                ))}
            </div>
            <div className="ml-auto">
                <Button size="sm" onClick={()=>{setQry((prev)=>({...prev, links: [...prev.links, {name: '', url: ''}]}))}}>Add New Link</Button>
            </div>
        </div>
    );
};