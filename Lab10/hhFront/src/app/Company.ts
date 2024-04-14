
export class Company {
    id : number ;
    name : string ;
    description : string ;
    city : string ;
    address : string ;

    constructor(id : number , name : string, description: string, city : string, address : string) { 
        this.id = id;
        this.name = name;
        this.description = description;
        this.city = city;
        this.address = address;
    }

}