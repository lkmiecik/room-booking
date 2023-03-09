import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

import { AppComponent } from './app.component';
import { NavMenuComponent } from './nav-menu/nav-menu.component';
import { HomeComponent } from './home/home.component';
import { BudynkiDataComponent } from './budynki-data/budynki-data.component';
import { RezerwujacyDataComponent } from './rezerwujacy-data/rezerwujacy-data.component';
import { SaleDataComponent } from './sale-data/sale-data.component';
import { RezerwacjeDataComponent } from './rezerwacje-data/rezerwacje-data.component';

@NgModule({
  declarations: [
    AppComponent,
    NavMenuComponent,
    HomeComponent,
    BudynkiDataComponent,
    RezerwujacyDataComponent,
    SaleDataComponent,
    RezerwacjeDataComponent,
  ],
  imports: [
    BrowserModule.withServerTransition({ appId: 'ng-cli-universal' }),
    HttpClientModule,
    FormsModule,
    RouterModule.forRoot([
      { path: '', component: HomeComponent, pathMatch: 'full' },
      { path: 'budynki-data', component: BudynkiDataComponent },
      { path: 'sale-data', component: SaleDataComponent },
      { path: 'rezerwacje-data', component: RezerwacjeDataComponent },
      { path: 'rezerwujacy-data', component: RezerwujacyDataComponent },
    ])
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
