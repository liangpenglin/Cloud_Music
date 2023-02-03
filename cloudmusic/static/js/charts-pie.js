/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */
//['Lavender Haze', 'Maroon', 'Antihero', 'Snow On The Beach', "You're On Your Own, Kid", 'Midnight Rain', 'Question...?', 'Vigilante Shit', 'Bejeweled', 'Labyrinth', 'Karma', 'Sweet Nothing', 'Mastermind', 'The Great War', 'Bigger Than The Whole Sky', 'Paris', 'High Infidelity', 'Glitch', "Would've, Could've, Should've", 'Dear Reader']
// [485, 601, 471, 538, 608, 544, 672, 614, 643, 727, 740, 648, 562, 674, 1171, 819, 1507, 1720, 1037, 898]
const pieConfig = {
  type: 'doughnut',
  data: {
    datasets: [
      {
        data: [289, 325, 275, 344, 396, 340, 407, 372, 392, 462, 472, 402, 367, 380, 747, 532, 958, 1214, 657, 582],
        /**
         * These colors come from Tailwind CSS palette
         * https://tailwindcss.com/docs/customizing-colors/#default-color-palette
         */
        backgroundColor: ['#68f23a','#f23ab2','#3a6ef2','#3ad6f2','#f24f3a','#f23ab2','#3AD6F2FF','#3a53f2','#6ef23a','#f2a83a',
        '#3a53f2','#6ef23a','#f2a83a','#3af2b2','#3af2d6','#68f23a','#f23ab2','#3a53f2','#6ef23a','#f2a83a',],
        label: 'Dataset 1',
      },
    ],
    labels: ['Lavender Haze', 'Maroon', 'Antihero', 'Snow On The Beach', "You're On Your Own, Kid", 'Midnight Rain', 'Question...?', 'Vigilante Shit', 'Bejeweled', 'Labyrinth', 'Karma', 'Sweet Nothing', 'Mastermind', 'The Great War', 'Bigger Than The Whole Sky', 'Paris', 'High Infidelity', 'Glitch', "Would've, Could've, Should've", 'Dear Reader'],
  },
  options: {
    responsive: true,
    cutoutPercentage: 80,
    /**
     * Default legends are ugly and impossible to style.
     * See examples in charts.html to add your own legends
     *  */
    legend: {
      display: false,
    },
  },
}

// change this to the id of your chart element in HMTL
const pieCtx = document.getElementById('pie')
window.myPie = new Chart(pieCtx, pieConfig)
