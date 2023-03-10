function FetchAPI(query, method) {
    return new Promise((resolve, reject) => {
        const params = {
            method: method,
            body: method != "GET" ? body : null
        }
 
        fetch(`/api/v1/${query}`).then( (result) => {
            resolve(result)
        }).catch(reject)
    })
}