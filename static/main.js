const GENES_SELECTOR            = document.getElementById('genes-selector');
const CONVERTED_GENE_CONTENT    = document.getElementById('converted-gene-content');
const SEARCH_INPUT              = document.getElementById('search-input')
const HARD_SEARCH_INPUT         = document.getElementById('hard-search-checkbox')
const SEARCH_BUTTON             = document.getElementById('search-button')

let convertedGen;

GENES_SELECTOR.addEventListener('change', (event) => {

    FetchAPI(`genes/${GENES_SELECTOR.value}`).then( (result) => {
        if (result.status != 200) { return; }

        CONVERTED_GENE_CONTENT.innerHTML = result.data.result.converted
        convertedGen = result.data.result.converted
    })
})
GENES_SELECTOR.dispatchEvent(new Event("change"))

// await FetchAPI("genes/82/search/HUGO")
SEARCH_BUTTON.addEventListener('click', () => {

    FetchAPI(`genes/${GENES_SELECTOR.value}/search/${SEARCH_INPUT.value}`).then( (result) => {
        if (result.status != 200) {
            CONVERTED_GENE_CONTENT.innerHTML = "Pas !"
            return
        }

        CONVERTED_GENE_CONTENT.innerHTML = "Trouvé !"
    })
})