import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SaleDataComponent } from './sale-data.component';

describe('SaleDataComponent', () => {
  let component: SaleDataComponent;
  let fixture: ComponentFixture<SaleDataComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SaleDataComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SaleDataComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
