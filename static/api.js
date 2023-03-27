function FetchAPI(query, method, body) {
    return new Promise((resolve, reject) => {
        const params = {
            method: method,
            headers: {
                "Content-Type": "application/json"
            },
            body: method != "GET" ? JSON.stringify(body) : null
        }

        fetch(`/api/v1/${query}`, params).then( (result) => {
            result.json().then( (formatedResult) => {
                resolve({
                    status: result.status,
                    data: formatedResult
                })
            })
        }).catch(reject)
    })
}