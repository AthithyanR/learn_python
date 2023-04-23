// const cluster = require('node:cluster')
// // const { availableParallelism } = require('node:os')

// if (cluster.isPrimary) {
//     // const numCPUs = availableParallelism();
//     for (let i = 0; i < 6; i++) {
//         cluster.fork();
//     }
//     cluster.on('exit', (worker, code, signal) => {
//         console.log(`worker ${worker.process.pid} died`);
//     });
// } else {
//     const http = require('node:http')
//     const resp = JSON.stringify({ message: 'hello' })
//     http.createServer((_req, res) => {
//         res.writeHead(200, { 'Content-Type': 'application/json' });
//         res.end(resp)
//     }).listen(8000, () => console.log('listening on port 8000'))
// }

const { exec } = require('node:child_process')
exec('./main.py', (err, stdout, stderr) => {
    process.stdout.write(stdout)
})