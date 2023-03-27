const GENES_SELECTOR            = document.getElementById('genes-selector');
const CONVERTED_GENE_CONTENT    = document.getElementById('converted-gene-content');
const SEARCH_INPUT              = document.getElementById('search-input');
const HARD_SEARCH_INPUT         = document.getElementById('hard-search-checkbox');
const SEARCH_BUTTON             = document.getElementById('search-button');
const ADD_DNA_BUTTON            = document.getElementById('add-dna-button');
const ADD_DNA_NAME_INPUT        = document.getElementById('add-dna-name-input')
const ADD_DNA_CONTENT_INPUT        = document.getElementById('add-dna-content-input')


String.prototype.replaceAt = function(index, replacement) {
    return this.substring(0, index) + replacement + this.substring(index + replacement.length);
}

let convertedGen;

GENES_SELECTOR.addEventListener('change', (event) => {

    FetchAPI(`genes/${GENES_SELECTOR.value}`).then( (result) => {
        if (result.status != 200) { return; }

        CONVERTED_GENE_CONTENT.innerHTML = result.data.result.converted
        convertedGen = result.data.result.converted
    })
})
GENES_SELECTOR.dispatchEvent(new Event("change"))

SEARCH_BUTTON.addEventListener('click', () => {

    FetchAPI(`genes/${GENES_SELECTOR.value}/search/${SEARCH_INPUT.value}${HARD_SEARCH_INPUT.checked ? "?hard-search=1" : ""}`).then( (result) => {
        if (result.status != 200) {
            CONVERTED_GENE_CONTENT.innerHTML = "Pas trouvé !"
            return
        }

        let formatedResult = convertedGen;
        let indexPlus = 0;
        result.data.result.occurences.forEach( (occurence) => {
            const newText = `<span style="color: red">${convertedGen[occurence]}</span>`;
            
            formatedResult = formatedResult
                .replaceAt(occurence + indexPlus, newText)

            indexPlus += newText.length - convertedGen[occurence].length
        })

        CONVERTED_GENE_CONTENT.innerHTML = formatedResult
    })
})

ADD_DNA_BUTTON.addEventListener("click", () => {
    FetchAPI(`genes`, "POST", {
        name: ADD_DNA_NAME_INPUT.value,
        content: ADD_DNA_CONTENT_INPUT.value
    }).then( () => {
        window.location.reload();
    })
})