import { Component } from '@angular/core';
import { faCircleXmark, faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { Filter } from '../../shared/models/filter.model';


@Component({
  selector: 'app-main',
  standalone: true,
  imports: [FontAwesomeModule],
  templateUrl: './main.component.html',
  styleUrl: './main.component.css'
})
export class MainComponent {
  filter: Filter = {
    posTags: [],
    negTags: [],
    experience: '',
    education: '',
  };

  search = faMagnifyingGlass;
  delete = faCircleXmark;

  posTags: string[] = [];

  negTags: string[] = [];

  searchCV() {
    this.filter.posTags = this.posTags;
    this.filter.negTags = this.negTags;
    // this.filter.education = this.
  }

  addPosTag(tag: any) {
    if(tag && !this.posTags.includes(tag)) {
      this.posTags.push(tag);
    }
  }

  choosePosTag(tag: string) {
    if(!this.posTags.includes(tag)) {
      this.posTags.push(tag);
    }
  }

  deletePosTag(index: number) {
    this.posTags = this.posTags.filter(el => el !== this.posTags[index]);
  }


  addNegTag(tag: any) {
    if(tag && !this.negTags.includes(tag)) {
      this.negTags.push(tag);
    }
  }

  chooseNegTag(tag: string) {
    if(!this.negTags.includes(tag)) {
      this.negTags.push(tag);
    }
  }

  deleteNegTag(index: number) {
    this.negTags = this.negTags.filter(el => el !== this.negTags[index]);
  }

  tagsPos = ['JS', 'Python', 'Angular', 'React']

  tags = ['Частая смена работы', 'Неготовность к переезду', 'Незнание англ.яз', 'Курящий']

}
