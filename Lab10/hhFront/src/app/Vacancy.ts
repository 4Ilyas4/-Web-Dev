
export class Vacancy {
    id : number ;
    name : string ;
    description : string ;
    salary : number ;
    company : number ;

    constructor(id : number , name : string, description: string, salary : number, company : number) { 
        this.id = id;
        this.name = name;
        this.description = description;
        this.salary = salary;
        this.company = company;
    }

}