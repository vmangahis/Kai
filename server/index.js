const exp = require('express');
const app = exp();


app.get('/', (req, res) => {
    
    return '';
})

app.listen(8999, () => {
    console.log('listening');
})