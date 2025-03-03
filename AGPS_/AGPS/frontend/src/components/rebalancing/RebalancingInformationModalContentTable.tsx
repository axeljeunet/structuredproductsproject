import React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';

// TODO CHange this to integrate data

function createData(
    productName: string,
    previousQuantity: number,
    newQuantity: number,
  ) {
    return { productName, previousQuantity, newQuantity };
  }
  
  const rows = [
    createData('Frozen yoghurt', 159, 6.0),
    createData('Ice cream sandwich', 237, 9.0),
    createData('Eclair', 262, 16.0),
    createData('Cupcake', 305, 3.7),
    createData('Gingerbread', 356, 16.0),
  ];
  
export default function RebalancingInformationModalContentTable() {
    return (
        <TableContainer component={Paper}>
            <Table sx={{ minWidth: 650 }} aria-label="simple table">
                <TableHead>
                <TableRow sx={{backgroundColor: '#6CB4EE'}}>
                    <TableCell> <Typography>Product name</Typography> </TableCell>
                    <TableCell> <Typography>Previous quantity</Typography> </TableCell>
                    <TableCell> <Typography>New quantity</Typography> </TableCell>
                </TableRow>
                </TableHead>
                <TableBody>
                {rows.map((row) => (
                    <TableRow
                    key={row.productName}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                    >
                    <TableCell component="th" scope="row">
                        <Typography> {row.productName} </Typography>
                    </TableCell>
                    <TableCell> <Typography>{row.previousQuantity} </Typography></TableCell>
                    <TableCell> <Typography> {row.newQuantity} </Typography></TableCell>
                    </TableRow>
                ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}
