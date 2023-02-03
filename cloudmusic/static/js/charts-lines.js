/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */


const lineConfig = {
  type: 'line',
  data: {
    labels: ['Lavender Haze', 'Maroon', 'Antihero', 'Snow On The Beach', "You're On Your Own, Kid", 'Midnight Rain', 'Question...?', 'Vigilante Shit', 'Bejeweled', 'Labyrinth', 'Karma', 'Sweet Nothing', 'Mastermind', 'The Great War', 'Bigger Than The Whole Sky', 'Paris', 'High Infidelity', 'Glitch', "Would've, Could've, Should've", 'Dear Reader'],
    datasets: [
      {
        label: 'Organic',
        /**
         * These colors come from Tailwind CSS palette
         * https://tailwindcss.com/docs/customizing-colors/#default-color-palette
         */
        backgroundColor: '#0694a2',
        borderColor: '#0694a2',
        data: [485, 601, 471, 538, 608, 544, 672, 614, 643, 727, 740, 648, 562, 674, 1171, 819, 1507, 1720, 1037, 898],
        fill: false,
      },

    ],
  },
  options: {
    responsive: true,
    /**
     * Default legends are ugly and impossible to style.
     * See examples in charts.html to add your own legends
     *  */
    legend: {
      display: false,
    },
    tooltips: {
      mode: 'index',
      intersect: false,
    },
    hover: {
      mode: 'nearest',
      intersect: true,
    },
    scales: {
      x: {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Month',
        },
      },
      y: {
        display: true,
        scaleLabel: {
          display: true,
          labelString: 'Value',
        },
      },
    },
  },
}

// change this to the id of your chart element in HMTL
const lineCtx = document.getElementById('line')
window.myLine = new Chart(lineCtx, lineConfig)
