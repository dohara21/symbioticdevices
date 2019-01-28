$(function() {
var chart    = document.getElementById('chart').getContext('2d'),
    gradient = chart.createLinearGradient(0, 0, 0, 450);

gradient.addColorStop(0, 'rgba(215, 225,83, 0.5)');
gradient.addColorStop(0.5, 'rgba(171, 209, 75, 0.5)');
gradient.addColorStop(1, 'rgba(121, 164, 71, 0.2)');


var data  = {
    labels: [ 'July', 'August', 'September', 'October', 'November', 'December', 'January', 'February', 'March', 'April', 'May', 'June'],
    datasets: [{
            label: '',
            backgroundColor: gradient,
            pointBackgroundColor: 'white',
            borderWidth: 1,
            borderColor: 'gray',
            data: [0, 10, 20, 35, 37, 45, 50, 50, 50, 50, 50, 100]
    }]
};


var options = {
    responsive: true,
    maintainAspectRatio: true,
    animation: {
        easing: 'easeInOutQuad',
        duration: 520
    },
    scales: {
        xAxes: [{
            gridLines: {
                color: 'rgba(215, 225, 83, 0.05)',
                lineWidth: 1
            }
        }],
        yAxes: [{
            gridLines: {
                color: 'rgba(200, 200, 200, 0.08)',
                lineWidth: 1
            }
        }]
    },
    elements: {
        line: {
            tension: 0.4
        }
    },
    legend: {
        display: false
    },
    point: {
        backgroundColor: 'white'
    },
    tooltips: {
        titleFontFamily: 'IBM Plex Sans',
        backgroundColor: 'rgba(0,0,0,0.7)',
        titleFontColor: 'white',
        caretSize: 5,
        cornerRadius: 2,
        xPadding: 10,
        yPadding: 10
    }
};


var chartInstance = new Chart(chart, {
    type: 'line',
    data: data,
        options: options
});
});
