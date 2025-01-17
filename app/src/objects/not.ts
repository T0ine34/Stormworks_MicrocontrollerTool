import { BaseElement } from './interface';

class Not extends BaseElement{
    x: number;
    y: number;
    id: string;

    constructor(x: number, y: number, id: string){
        super(x, y, id);
    }

    serialize(component_number : number, component_states_length : number): [XMLDocument, XMLDocument] {
        const component = new DOMParser().parseFromString(`
<c>
    <object id="${this.id}">
        <pos x="${this.x}" y="${this.y}"/>
    </object>
</c>`, 'text/xml');
        const component_state = new DOMParser().parseFromString(`
<c${component_states_length+1} id="${this.id}">
    <pos x="${this.x}" y="${this.y}"/>
</c${component_states_length+1}>`, 'text/xml');
        return [component, component_state];
    }

    load(data: XMLDocument): void {
        this.x = parseInt(data.querySelector('pos').getAttribute('x'));
        this.y = parseInt(data.querySelector('pos').getAttribute('y'));
    }