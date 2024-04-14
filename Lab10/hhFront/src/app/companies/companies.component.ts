import { Component, OnInit } from '@angular/core';
import { Company } from '../Company';
import { CompanyService } from '../company-service.service';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-companies',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  templateUrl: './companies.component.html',
  styleUrl: './companies.component.css'
})
export class CompaniesComponent implements OnInit {
  companylist!: Observable<Company[]>;

  constructor(
    private companyService: CompanyService
  ) {}

  ngOnInit(): void {
    this.companylist = this.companyService.getCompanies();
  }
}
