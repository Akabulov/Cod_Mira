# GaussAI

**GaussAI** - это веб-базированная интеллектуальная система, которая использует модели обработки естественного языка (NLP)
для резюме скрининга и классификации. Позволяя обрабатывать большое количество резюме в кратчайшие сроки, и выдавать наиболее
релевантные резюме, система классифицирует при этом обработанные резюме. Также наша система решит проблему ПОИСКА резюме,
так-как система может исследовать базы данных резюме, и получать список релевантных кандидатов по указанным критериям.

На данный момент у нас готов фундамент вебсайта, написана база скрипта-классификатора, а также написана начальная версия модели обработки естественного языка.

# Gauss Team

Используемые библиотеки:
Nltk, Spacy, Tkinter, Pyresparser, Pdfminer3, Aspose, PyPDF2, Tensorflow, Sklearn

Используемые модели:
Custom Keras KNN

Архитектура:
Веб-сервис на Angular с использованием NLP

This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 13.2.1.


## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via a platform of your choice. To use this command, you need to first add a package that implements end-to-end testing capabilities.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.
