import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Vacancy } from '../Vacancy';
import { CompanyService } from '../company-service.service';

@Component({
  selector: 'app-vacancy',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './vacancy.component.html',
  styleUrl: './vacancy.component.css'
})
export class VacancyComponent implements OnInit{
  vacancy! : Vacancy;

  constructor(
    private route: ActivatedRoute,
    private companyService: CompanyService
  ){}
  ngOnInit(): void {
    const vacancyId = this.route.snapshot.paramMap.get('id');
    if (vacancyId) {
      this.companyService.getVacancyById(parseInt(vacancyId)).subscribe(
        (vacancy : Vacancy) => {
          this.vacancy = vacancy;
        }
      );
    }
  }
}
