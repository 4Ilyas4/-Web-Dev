import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Company } from './Company';
import { Observable } from 'rxjs';
import { Vacancy } from './Vacancy'

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  private apiUrl = 'http://127.0.0.1:8000/api'

  constructor(private http: HttpClient) { }

  getVacancyById(id: number): Observable<Vacancy> {
    return this.http.get<Vacancy>(`${this.apiUrl}/vacancies/${id}/`);
  }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(`${this.apiUrl}/companies`);
  }

  getCompanyById(id: number): Observable<Company> {
    return this.http.get<Company>(`${this.apiUrl}/companies/${id}/`);
  }

  getVcancyListByCompany(id: number): Observable<Vacancy[]> {
    return this.http.get<Vacancy[]>(`${this.apiUrl}/companies/${id}/vacancies/`)
  }
}
