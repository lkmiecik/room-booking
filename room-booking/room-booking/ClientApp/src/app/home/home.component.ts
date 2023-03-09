import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
})
export class HomeComponent {

  constructor(public router: Router){}

  navigateToData(){
    this.router.navigate(['rezerwacje-data']);
    console.log("navigate");
  }
}
