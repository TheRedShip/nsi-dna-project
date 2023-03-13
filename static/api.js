function FetchAPI(query, method, body) {
    return new Promise((resolve, reject) => {
        const params = {
            method: method,
            body: method != "GET" ? body : null
        }
 
        fetch(`/api/v1/${query}`).then( (result) => {
            result.json().then( (formatedResult) => {
                resolve({
                    status: result.status,
                    data: formatedResult
                })
            })
        }).catch(reject)
    })
}