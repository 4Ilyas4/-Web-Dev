import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Company } from '../Company';
import { CompanyService } from '../company-service.service';
import { Vacancy } from '../Vacancy';

@Component({
  selector: 'app-company-details',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './company-details.component.html',
  styleUrls: ['./company-details.component.css']
})
export class CompanyDetailsComponent implements OnInit {
  company!: Company;
  vacancyList!: Vacancy[];
  constructor(
    private route: ActivatedRoute,
    private companyService: CompanyService
  ) {}

  ngOnInit(): void {
    const companyId = this.route.snapshot.paramMap.get('id');
    if (companyId) {
      this.companyService.getCompanyById(parseInt(companyId)).subscribe(
        (company: Company) => {
          this.company = company; 
        }
      );
      this.companyService.getVcancyListByCompany(parseInt(companyId)).subscribe(
        (vacancyList: Vacancy[]) => {
          this.vacancyList = vacancyList;
        }
      );
    }
  }
}
