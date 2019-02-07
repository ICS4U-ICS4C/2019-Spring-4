function A1(){
	var fName = prompt("Hey, what's your name?", name);
	var myColour = prompt("Pick a colour, "+fName);

	if (myColour == "red"){
		console.log("Looks like this guy likes red. Noted")
	} else if (myColour == "yellow"){
		console.log("This guy chose yellow. Hmm")
	} else {
		console.log(fname+" chose a colour I hadn't thought of: "+myColour)
	}

}
