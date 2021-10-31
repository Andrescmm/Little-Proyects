//
//  ViewController.swift
//  Light
//
//  Created by Andres  on 25/10/21.
//

import UIKit


class ViewController: UIViewController {
    
    var ligthOn = true

    
    override func viewDidLoad() {
        super.viewDidLoad()
        updateUi()
    }

    // Function
    func updateUi() {
        view.backgroundColor = ligthOn ? .white : .black
    }
    
    // Button Action
    @IBAction func buttonPressed(_ sender: Any) {
        ligthOn.toggle()
        updateUi()
    }
    
}

