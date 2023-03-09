import { Component, OnInit } from '@angular/core';
import { Rezerwujacy } from '../models/rezerwujacy';
import { DatabaseServiceService } from '../shared/database-service.service';

@Component({
  selector: 'app-rezerwujacy-data',
  templateUrl: './rezerwujacy-data.component.html',
  styleUrls: ['./rezerwujacy-data.component.css']
})
export class RezerwujacyDataComponent implements OnInit {
  rezerwujace: Rezerwujacy[] | undefined = [];

  constructor(public database: DatabaseServiceService) { }

  ngOnInit(): void {
    this.database.GetRezerwujacies().subscribe((rezerwujace: Rezerwujacy[]) => {
      this.rezerwujace = rezerwujace;
      console.log()
    })
  }

}
