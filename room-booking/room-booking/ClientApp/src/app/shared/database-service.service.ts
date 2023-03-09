import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Budynek } from '../models/budynki';
import { Rezerwacja } from '../models/rezerwacje';
import { Rezerwujacy } from '../models/rezerwujacy';
import { Sala } from '../models/sala';

@Injectable({
  providedIn: 'root'
})
export class DatabaseServiceService {

  constructor(private http: HttpClient) { }

  GetBudynkis(){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.get<Budynek[]>("api/Budynkis", {headers: headers} )
  }

  GetBudynki(id: Number){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.get<Budynek>("api/Budynkis/" + id.toString(), {headers: headers} )
  }

  PutBudynki(id: Number, budynek: Budynek){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.put<Budynek>("api/Budynkis/" + id.toString(), budynek ,{headers: headers} )
  }

  PostBudynki(budynek: Budynek){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.post<Budynek>("api/Budynkis", budynek ,{headers: headers} )
  }

  DeleteBudynki(id: number){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.delete<Budynek>("api/Budynkis/" + id.toString(), {headers: headers} )
  }

  GetRezerwacjes(){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.get<Rezerwacja[]>("api/Rezerwacjes", {headers: headers} )
  }

  GetRezerwacje(id: Number){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.get<Rezerwacja>("api/Rezerwacjes/" + id.toString(), {headers: headers} )
  }

  PutRezerwacje(id: Number, rezerwacja: Rezerwacja){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.put<Rezerwacja>("api/Rezerwacjes/" + id.toString(), rezerwacja, {headers: headers} )
  }

  PostRezerwacje(rezerwacja: Rezerwacja){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.post<Rezerwacja>("api/Rezerwacjes", rezerwacja, {headers: headers} )
  }

  DeleteRezerwacje(id: Number){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.delete<Rezerwacja>("api/Rezerwacjes/" + id.toString(), {headers: headers} )
  }

  GetRezerwujacies(){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.get<Rezerwujacy[]>("api/Rezerwujacies", {headers: headers} )
  }

  GetRezerwujacy(id: Number){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.get<Rezerwujacy>("api/Rezerwujacies", {headers: headers} )
  }

  PutRezerwujacy(id: Number, rezerwujacy: Rezerwujacy){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.put<Rezerwujacy>("api/Rezerwujacies/" + id.toString(), rezerwujacy, {headers: headers} )
  }

  PostRezerwujacy(rezerwujacy: Rezerwujacy){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.post<Rezerwujacy>("api/Rezerwujacies", rezerwujacy, {headers: headers} )
  }

  DeleteRezerwujacy(id: Number){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.delete<Rezerwujacy>("api/Rezerwujacies" + id.toString(), {headers: headers} )
  }

  GetSales(){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.get<Sala[]>("api/Sales", {headers: headers} )
  }

  GetSale(id: Number){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.get<Sala>("api/Sales/" + id.toString(), {headers: headers} )
  }

  PutSale(id: Number, sala: Sala){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.put<Sala>("api/Sales/" + id.toString(), sala, {headers: headers} )
  }

  PostSale(sala: Sala){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.post<Sala>("api/Sales", sala, {headers: headers} )
  }

  DeleteSale(id: Number){
    let headers = new HttpHeaders()
    .set('content-type', 'application/json')
    .set('Access-Control-Allow-Origin', '*');
    return this.http.delete<Sala>("api/Sales/" + id.toString(), {headers: headers} )
  }
}
