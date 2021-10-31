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
    fileprivate func updateUi() {
        if ligthOn{
            ///lightButton.setTitle("Off", for: .normal)
            view.backgroundColor = .white
        }
        else{
            ///lightButton.setTitle("On", for: .normal)
            view.backgroundColor = .black
        }
    }
    
    // Button Action
    @IBAction func buttonPressed(_ sender: Any) {
        ligthOn.toggle()
        updateUi()
    }
    
}

