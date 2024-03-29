// generate interface 
function generateInterface(listFile) {

    $("#interfaceBtn").css("display", "none")

    s = `
    <br>
    <br>
    <form id="box" action="https://proteinformatics.uni-leipzig.de/mutation_explorer_delta/interface" method="post" enctype="multipart/form-data" target="_blank" style="margin-left: 20px">

        Select alignment, Friend <br>
        
        <select id='fileDropdownConv' name='alignment_link' onchange='changeSeqSelectionConv()'></select>
        <br>
        <br>

        <!-- Upload a PDB <br> -->
        Provide a Protein Data Bank identifier (4 characters) or upload a coordinate file <br>

        <input id="pdbConv" name="pdb_conv" type="text" placeholder="Enter PDB ID" onchange="clearInput('#fileConv')" required><br>
        <input id="fileConv" name="file_conv" type="file" accept=".pdb" onchange="clearInput('#pdbConv')" required>
        <br>


        <!-- Upload a second PDB (optional, structures get aligned/superimposed) <br> -->
        Provide a second identifier or select a file for upload (optional, structures will be superposed) <br>

        <input id="pdbSuper" name="pdb_super" type="text" placeholder="Enter PDB ID" onchange="clearInput('#fileSuper')"><br>
        <input id="fileSuper" name="file_super" type="file" accept=".pdb" onchange="clearInput('#pdbSuper')">
        <br>

        Uploading a single PDB may take up to 20 seconds, uploading two PDBs up to 1 minute.
        <br>

        <input type="submit">
    </form>
    `;
    $("#box").append(s);


    // add alignments to dropdown
    fetch(listFile)
        .then(response => response.text())
        .then(text => text.split("\n"))
        .then(files => {
            for (let i = 0; i < files.length; i++) {
                fsplit = `${files[i]}`.split("/");
                filename = fsplit[fsplit.length - 1];
                $("#fileDropdownConv").append(`<option value='${files[i]}'>${filename}</option>`);
            }
        });



    //changeSeqSelectionConv()


    var $inputs = $('input[name=pdb_conv],input[name=file_conv]');
    $inputs.on('input', function () {
        // Set the required property of the other input to false if this input is not empty.
        $inputs.not(this).prop('required', !$(this).val().length);
    });
}




function clearInput(el) {
    $(el).val("");
} 












/*
function changeSeqSelection() {
    file = $("#fileDropdown").children("option:selected").val();
    fetch(file)
        .then(response => response.text())
        //.then(text => console.log(text))
        .then(text => text.split("\n"))
        .then(lines => [lines[2].split(/[ ]+/)[0], lines[3].split(/[ ]+/)[0]])
        .then(arr => {
            $("#seqA").children().remove();
            $("#seqB").children().remove();
            for (let i = 0; i < arr.length; i++) {
                $("#seqA").append(`<option value='${arr[i]}'>${arr[i]}</option>`);
                $("#seqB").append(`<option value='${arr[i]}'>${arr[i]}</option>`);
            }
        });
}
*/

