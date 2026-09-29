import fs from 'node:fs/promises';
import {FileBlob, SpreadsheetFile} from '@oai/artifact-tool';
const out = new URL('.',import.meta.url).pathname.replace(/^\/([A-Za-z]:)/,'$1');
const wb=await SpreadsheetFile.importXlsx(await FileBlob.load('C:/Users/Marc/Documents/MotorHome/Sum of last digits.xlsx'));
const s=wb.worksheets.getItem('Sheet1');
if(process.argv[2]==='before') {
 const p=await wb.render({sheetName:'Sheet1',range:'A1:G25',scale:1,format:'png'});
 await fs.writeFile(out+'before.png',new Uint8Array(await p.arrayBuffer()));
} else {
 s.getRange('G2:G25').formulas=Array.from({length:24},(_,i)=>[`=SUM(A${i+2}:E${i+2})`]);
 wb.recalculate();
 console.log((await wb.inspect({kind:'table',range:'Sheet1!A1:G25',include:'values,formulas',tableMaxRows:25,tableMaxCols:7})).ndjson);
 const p=await wb.render({sheetName:'Sheet1',range:'A1:G25',scale:1,format:'png'});
 await fs.writeFile(out+'after.png',new Uint8Array(await p.arrayBuffer()));
 await (await SpreadsheetFile.exportXlsx(wb)).save(out+'Sum of last digits.xlsx');
}
