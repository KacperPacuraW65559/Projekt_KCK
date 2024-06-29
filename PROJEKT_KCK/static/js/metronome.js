let intervalId = null;
let tempo = 120;

function playMetronomeClick() {
    const metronomeTick = document.getElementById('metronomeTick');
    metronomeTick.currentTime = 0;
    metronomeTick.play();
}

document.getElementById('startMetronomeBtn').addEventListener('click', function() {
    if (intervalId) clearInterval(intervalId);
    intervalId = setInterval(playMetronomeClick, 60000 / tempo);
});

document.getElementById('stopMetronomeBtn').addEventListener('click', function() {
    clearInterval(intervalId);
});

document.getElementById('tempoSlider').addEventListener('input', function(event) {
    const newTempo = event.target.value;
    updateTempoDisplay(newTempo);
});

function updateTempoDisplay(newTempo) {
    document.getElementById('tempoDisplay').textContent = newTempo;
    tempo = newTempo;
    if (intervalId) {
        clearInterval(intervalId);
        intervalId = setInterval(playMetronomeClick, 60000 / tempo);
    }
}
