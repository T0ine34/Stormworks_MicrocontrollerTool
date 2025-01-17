export class BaseElement{
    x: number;
    y: number;
    id: string;

    constructor(x: number, y: number, id: string){
        this.x = x;
        this.y = y;
        this.id = id;
    }

    /**
     * Serialize the object to a xml string
     * @param component_number The unique number of the component
     * @returns two XMLDocuments, the first goes into components, the second goes into component_states
     */
    serialize(component_number : number, component_states_length : number): [XMLDocument, XMLDocument] {
        throw new Error('Not implemented');
    }

    /**
     * Load the object from a xml string
     * @param data The XMLDocument to load from, coming from components
     */
    load(data: XMLDocument): void {
        throw new Error('Not implemented');
    }

    draw(ctx: CanvasRenderingContext2D): void {
        throw new Error('Not implemented');
    }
}