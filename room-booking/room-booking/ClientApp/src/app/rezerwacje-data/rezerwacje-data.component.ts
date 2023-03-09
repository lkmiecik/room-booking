import { Component, OnInit } from '@angular/core';
import { Rezerwacja } from '../models/rezerwacje';
import { DatabaseServiceService } from '../shared/database-service.service';

@Component({
  selector: 'app-rezerwacje-data',
  templateUrl: './rezerwacje-data.component.html',
  styleUrls: ['./rezerwacje-data.component.css']
})
export class RezerwacjeDataComponent implements OnInit {
  rezerwacje: Rezerwacja[] | undefined = [];

  constructor(public database: DatabaseServiceService) { }

  ngOnInit(): void {
    this.database.GetRezerwacjes().subscribe((rezerwacje: Rezerwacja[]) => {
      this.rezerwacje = rezerwacje;
      console.log(rezerwacje);
    })
  }
}
