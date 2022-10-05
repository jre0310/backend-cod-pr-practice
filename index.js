const cod = require('call-of-duty-api');
const app = require('express')();
const PORT = 8080;

const token = 'ODU0MzAzNTIzOTM1OTg0MjI4MzoxNjY2MTUxODA5NzE3OmY2OTEzOWQzZTYxNWVlMzZhMzQyYjI5NDNhMjZhMWZi'
let gamertag = 'stltank91#1618'

console.log('Program started...')

app.listen(
    PORT,
    () => console.log(`its running on http://localhost:${PORT}`)
);

app.get('/health-check', (req, res) => {
    res.status(200).send({
        status: 'Up and Running'
    })
})

app.post('/post-test', (req, res) => {


})

// cod.login(token);

// const getStats = async () => {
//     try {
//         let data = await cod.Warzone.fullData(gamertag, cod.platforms.Battlenet)
//         console.log(data.data.lifetime.all);
//     } catch (error) {
//         console.error(error)
//     }
// }

// getStats();



















