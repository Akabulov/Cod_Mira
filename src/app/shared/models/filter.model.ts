export class Filter {
    posTags: string[];
    negTags: string[];
    experience: string;
    education: string;

    constructor(posTags: string[], negTags: string[], experience: string, education: string) {
        this.posTags = posTags;
        this.negTags = negTags;
        this.experience = experience;
        this.education = education;
    }
}
