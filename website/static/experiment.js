ExperimentController = function(images) {
    this.images = images;   
    this.index = 0;
    this.results = [];
    var self = this;
    
    this.now = function() {
        return (new Date()).getTime();
    }

    this.start = function() {
        $('#startup, #imageBrowser').toggle();
        this.index = 0;
        this.startTime = this.now();
    }
    
    this.onClick = function(humanInImage) {
        var image = this.images[this.index];
        var entry = {
            id : image["id"],
            selection : humanInImage,
            time : this.now() - this.startTime
        };
        this.results.push(entry);
        this.index = this.index+1;
        if (this.index == this.images.length) {
            $('#container').hide();

            $('#results').val(JSON.stringify(this.results));
            $('#resultsForm').submit();
        }
        else {
            $('#slideshow').cycle(this.index); 
        }
    }
    
    $('#imageBrowser').toggle();
    
    $('#startButton').click(function() {
        self.start();
    });
    
    $('#noButton').click(function(){
        self.onClick(false);
    });
    
    $('#yesButton').click(function(){
        self.onClick(true);
    });
    
    $('#slideshow').cycle({ 
        timeout: 0, 
        fx:     'scrollHorz',
        speed:  'fast',
        startingSlide: 0 
    });
}

