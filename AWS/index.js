'use stsrict'

/*
Frameworks:
    Claudia.js (JS)
    APEX serverless architecture
    SERVER LESS
    SPARTA
    Chalice
    Zappa 
*/
exports.handler = (event, context, callback) => {
    
    callback(null, {
        statusCode: 500,
        body: 'Something went wrong'
    })
}