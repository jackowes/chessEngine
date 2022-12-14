//This code is from https://chessboardjs.com/examples#5003
//Highlight Legal Moves
// NOTE: this example uses the chess.js library:
// https://github.com/jhlywa/chess.js

// --- IMPORTS ---

import { Chess } from './chess.js'

// --- GLOBAL VARIABLES ---

var board = null
var fenStart = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
var fenEmpty = '8/8/8/8/8/8/8/8 w - - 0 1'
var game = new Chess(fenStart)
var whiteSquareGrey = '#a9a9a9'
var blackSquareGrey = '#696969'
var config = {
  draggable: true,
  position: fenStart,
  onDragStart: onDragStart,
  onDrop: onDrop,
  onMouseoutSquare: onMouseoutSquare,
  onMouseoverSquare: onMouseoverSquare,
  onSnapEnd: onSnapEnd,
  onChange: onChange
}

// --- FUNCTIONS ---

function removeGreySquares () {
  $('#main-board .square-55d63').css('background', '')
}

function greySquare (square) {
  var $square = $('#main-board .square-' + square)

  var background = whiteSquareGrey
  if ($square.hasClass('black-3c85d')) {
    background = blackSquareGrey
  }

  $square.css('background', background)
}

function onDragStart (source, piece) {
  // do not pick up pieces if the game is over
  if (game.game_over()) return false

  // or if it's not that side's turn
  if ((game.turn() === 'w' && piece.search(/^b/) !== -1) ||
      (game.turn() === 'b' && piece.search(/^w/) !== -1)) {
    return false
  }
}

function onDrop (source, target) {
  removeGreySquares()

  // see if the move is legal
  var move = game.move({
    from: source,
    to: target,
    promotion: 'q' // NOTE: always promote to a queen for example simplicity
  })

  // illegal move
  if (move === null) return 'snapback'
}

function onMouseoverSquare (square, piece) {
  // get list of possible moves for this square
  var moves = game.moves({
    square: square,
    verbose: true
  })

  // exit if there are no moves available for this square
  if (moves.length === 0) return

  // highlight the square they moused over
  greySquare(square)

  // highlight the possible squares for this piece
  for (var i = 0; i < moves.length; i++) {
    greySquare(moves[i].to)
  }
}

function onMouseoutSquare (square, piece) {
  removeGreySquares()
}

function onSnapEnd () {
  board.position(game.fen())
}

// Called when the game is over
function checkGameEnd() {
  // detect draws and stalemates
  if(game.in_draw() || game.in_stalemate()) {
    document.getElementById('game-result').innerHTML += '<br>Draw';
  }

  // detect losing side
  if(game.in_checkmate()) {
    if(game.turn() == 'b') {
      document.getElementById('game-result').innerHTML += 'White Wins';
    }
    else {
      document.getElementById('game-result').innerHTML += 'Black Wins';
    }
  }
}

function onChange() {
  console.log('pos changed')
  console.log(game.ascii())
  console.log(game.fen())
  checkGameEnd()
}

function newGameButtonOnClick() {
  game = new Chess() //reset chess.js game
  board.start() //reset chessboard
  document.getElementById('game-result').innerHTML = "" //reset HTML result
}

// --- MAIN ---

function main() {
  board = Chessboard('main-board', config)
  checkGameEnd()

  document.getElementById("new-game-button").addEventListener("click", newGameButtonOnClick)
}

main()
