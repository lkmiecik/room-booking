import { Component, OnInit } from '@angular/core';
import { Sala } from '../models/sala';
import { DatabaseServiceService } from '../shared/database-service.service';

@Component({
  selector: 'app-sale-data',
  templateUrl: './sale-data.component.html',
  styleUrls: ['./sale-data.component.css']
})
export class SaleDataComponent implements OnInit {
  sale: Sala[] | undefined = [];

  constructor(public database: DatabaseServiceService) { }

  ngOnInit(): void {
    this.database.GetSales().subscribe((sale: Sala[]) => {
      this.sale = sale;
      console.log(sale);
    });
  }

}
