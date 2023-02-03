/**
 * For usage, visit Chart.js docs https://www.chartjs.org/docs/latest/
 */

const barConfig = {

  type: 'bar',
  data: {
    labels: ['Lavender Haze', 'Maroon', 'Antihero', 'Snow On The Beach', "You're On Your Own, Kid", 'Midnight Rain', 'Question...?', 'Vigilante Shit', 'Bejeweled', 'Labyrinth', 'Karma', 'Sweet Nothing', 'Mastermind', 'The Great War', 'Bigger Than The Whole Sky', 'Paris', 'High Infidelity', 'Glitch', "Would've, Could've, Should've", 'Dear Reader'],
    datasets: [
      {
        label: 'pos',
        backgroundColor: '#0694a2',
        // borderColor: window.chartColors.red,
        borderWidth: 1,
        data: [260, 389, 271, 328, 417, 329, 422, 364, 378, 448, 395, 476, 368, 461, 795, 526, 896, 884, 673, 591],
      },
      {
        label: 'neu',
        backgroundColor: '#7e3af2',
        // borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: [157, 157, 133, 134, 130, 141, 156, 184, 180, 194, 234, 121, 124, 150, 264, 200, 351, 599, 236, 200],
      },
      {
        label: 'neg',
        backgroundColor: '#1c64f2',
        // borderColor: window.chartColors.blue,
        borderWidth: 1,
        data: [68, 55, 67, 76, 61, 74, 94, 66, 85, 85, 111, 51, 70, 63, 112, 93, 260, 237, 128, 107],
      },
    ],
  },
  options: {
    responsive: true,
    legend: {
      display: false,
    },
  },
}

const barsCtx = document.getElementById('bars')
window.myBar = new Chart(barsCtx, barConfig)
