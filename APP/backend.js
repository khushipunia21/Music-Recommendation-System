alert("backend")
const {spawn}=require('child_process');
// var input='Symbiote'
const childPython=spawn('python',['model.py','Born 2 Live']);

childPython.stdout.on('data',(data) => {
    console.log(`stdout: ${data}`);
});

childPython.stderr.on('data',(data)=> {
    console.error(`stderr: ${data}`);
});
