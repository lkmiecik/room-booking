import { Component, OnInit } from '@angular/core';
import { DatabaseServiceService } from '../shared/database-service.service';
import { Budynek } from '../models/budynki';

@Component({
  selector: 'app-budynki-data',
  templateUrl: './budynki-data.component.html',
  styleUrls: ['./budynki-data.component.css']
})
export class BudynkiDataComponent implements OnInit {
  budynki: Budynek[] | undefined = []; 

  constructor(public database: DatabaseServiceService) { }

  ngOnInit(): void {
    this.database.GetBudynkis().subscribe((budynki: Budynek[]) => {
      this.budynki = budynki;
      console.log(budynki);
    });
  }

}
