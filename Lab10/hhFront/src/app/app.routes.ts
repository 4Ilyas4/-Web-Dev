import { Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { CompanyDetailsComponent } from './company-details/company-details.component';
import { CompaniesComponent } from './companies/companies.component';
import { VacancyComponent } from './vacancy/vacancy.component';

export const routes: Routes = [
    { path: '', redirectTo: '/home', pathMatch: 'full'}, 
    { path: 'vacancies/:id', component: VacancyComponent}, 
    { path: 'companies', component: CompaniesComponent},
    { path: 'companies/:id', component: CompanyDetailsComponent},
    { path: '**', component: HomeComponent},
];
