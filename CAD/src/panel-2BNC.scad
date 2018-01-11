
module mainBody() {    
    color("Red")
    translate([2,2,0]) 
    minkowski() {
        $fn=30;
        cube([110-4,55-4,1.5/2]); 
        cylinder(r=2,h=1.5/2);
        }    
}

module bigFrame() {
    color("Red") cube([53,18,10]); 
}

module smallFrame() {
    color("Green") cube([10,10,5]); 
}

module innerFrame() {    
    //color("Red")
    translate([2,2,0]) 
    minkowski() {
        $fn=30;
        cube([89.5-4,35.5-4,1.2/2]); 
        cylinder(r=2,h=1.2/2);
        }   
}

module hole() {
    color("blue") cylinder($fn=40, h=10, r=1.6);
}

module holderBNC() {
    color("blue") cylinder($fn=40, h=2.7, r=8);
}

module holeBNC() {
    color("green") cylinder($fn=40, h=11, r=5);
}

module body() {
    union() {
        mainBody();
        translate([10.25,9.75,1.3]) innerFrame();
        translate([30,27.5,2.3]) holderBNC();
        translate([80,27.5,2.3]) holderBNC();
        }
}

module object(){
    difference() {
        body();    
        translate([30,27.5,-5]) holeBNC();    
        translate([80,27.5,-5]) holeBNC();
        translate([4,4,-5]) hole();
        translate([4,51,-5]) hole();
        translate([106,4,-5]) hole();
        translate([106,51,-5]) hole();
    }    
}

object();


/*
difference() {
    cube(30, center=true);
    sphere(20);
}
translate([0, 0, 30]) {
    cylinder(h=40, r=10);
}
    */