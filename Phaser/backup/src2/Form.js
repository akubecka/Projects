import React, {Component} from 'react'
import { Renderer } from 'phaser';
import { Page, Text, View, Document, StyleSheet } from '@react-pdf/renderer';
import ReactPDF from '@react-pdf/renderer';

  

  //ReactPDF.render(<MyDocument />, `${__dirname}/example.pdf`);
/* 
function Form(){
    function pdfer(){
        const input = fs.createReadStream('input.tex');
        const output = fs.createWriteStream('output.pdf');
        const pdf = latex(input);
    
        pdf.pipe(output);
        pdf.on('error', err => console.error(err));
        pdf.on('finish', () => console.log('PDF generated!'));
    }



    return(
        <div>
            {pdfer};
        </div>
    )
}
export default Form; */




class Form extends Component{
    constructor(props){
        super(props)

        this.state = {
            username: props.user,
            url: ''
        }
    }
    handlePicChange = async (event) => {
        this.setState({
            url: event.target.value
        })
        let bod= {username: this.state.username, newPhoto: this.state.url}
        const response = await fetch("http://localhost:3001/api/uploadNewPhoto",{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
                },
            body: JSON.stringify(bod)
        })
    }
    render(){
        return(
            <form>
                <div>
                    <label>Choose Profile Picture</label>
                    <select value ={this.state.url} onChange={this.handlePicChange}>
                        <option value="../../public/images/banana.jpg">Banana</option>
                        <option value="../../public/images/blueberry.jpg">Blueberry</option>
                        <option value="../../public/images/default.jpg">Default</option>
                        <option value="../../public/images/strawberry.jpg">Strawberry</option>
                        <option value="../../public/images/watermelon.jpg">Watermelon</option>
                    </select>
                    <input type='text' value = {this.state.url}/>
                </div>
            </form>
        )
    }
}export default Form;
