


<table style="width:100%">
    <tr>
        <td colspan="2" align="center"><strong>source</strong></td>
    </tr>
    <tr>
        <td colspan="2">
            '\'https://duplicatedemo.notesquare.com/assets/2012/10/13.jpg\''
            <br>
            https://duplicatedemo.notesquare.com/assets/2012/10/13.jpg
        </td>
    </tr>
    <tr>
        <th>regex</th>
        <th colspan="2">result</th>
    </tr>
    <tr>
        <td>
            .*(http.*[assets$]).*
            <br>
            .*(http:|https:.+?(?<=assets)).*
        </td>
        <td>https://duplicatedemo.notesquare.com/assets</td>    
    </tr>
    <tr>
        <td>.*((?<=assets).*\.(?:jpg|gif|png|jpeg))</td>
        <td>/2012/10/13.jpg</td>    
    </tr>

</table>


<br>
<table style="width:100%">
    <tr>
        <td colspan="2" align="center"><strong>source</strong></td>
    </tr>
    <tr>
        <td colspan="2">aabvasdD:/sarawakjobs/duplicatedemo.notesquare.com_origin/duplicatedemo.notesquare.com_edit/home/wp-content/uploads/2012/10/13.jpg'ashdjasd</td>
    </tr>
    <tr>
        <th>regex</th>
        <th colspan="2">result</th>
    </tr>
    <tr>
        <td>([^\/]*.(?:jpg|gif|png|jpeg))</td>
        <td>13.jpg</td>    
    </tr>
    <tr>
        <td>([a-zA-Z]:\/.*?\/)((?:[^\/]|\\\/)+?)(?:(?<!\\)\s|$)</td>
        <td>D:/sarawakjobs/duplicatedemo.notesquare.com_origin/duplicatedemo.notesquare.com_edit/home/wp-content/uploads/2012/10/</td>    
    </tr>
    <tr>
        <td>(\/.*?\/)((?:[^\/]|\\\/)+?)(?:(?<!\\)\s|$)</td>
        <td>/sarawakjobs/duplicatedemo.notesquare.com_origin/duplicatedemo.notesquare.com_edit/home/wp-content/uploads/2012/10/</td>    
    </tr>
    <tr>
        <td>.*((?<=uploads).*\.(?:jpg|gif|png|jpeg))</td>
        <td>/2012/10/13.jpg</td>    
    </tr>
    <tr>
        <td>.*((?>uploads).*\.(?:jpg|gif|png|jpeg))</td>
        <td>uploads/2012/10/13.jpg</td>    
    </tr>
    <tr>
        <td>.*((?>\/uploads).*\.(?:jpg|gif|png|jpeg))</td>
        <td>/uploads/2012/10/13.jpg</td>    
    </tr>

</table>
<br>
<table style="width:100%">
    <tr>
        <td colspan="2" align="center"><strong>source</strong></td>
    </tr>
    <tr>
        <td colspan="2">D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\Test-1-employer.jpg'</td>
    </tr>
    <tr>
        <th>regex</th>
        <th colspan="2">result</th>
    </tr>
    <tr>
        <td>([a-zA-Z]:\\.*?\\)((?:[^\\]|\\\/)+?)(?:(?<!\\)\s|$)</td>
        <td>D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\</td>
    </tr>
    <tr>
        <td>([^\\]*.(?:jpg|gif|png|jpeg))</td>
        <td>Test-1-employer.jpg</td>
    </tr>
    

</table>

<table style="width:100%">
    <tr>
        <td colspan="2" align="center"><strong>source</strong></td>
    </tr>
    <tr>
        <td colspan="2">D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\Test-1-employer.jpg'</td>
    </tr>
    <tr>
        <th>regex</th>
        <th colspan="2">result</th>
    </tr>
    <tr>
        <td>([a-zA-Z]:\\.*?\\)((?:[^\\]|\\\/)+?)(?:(?<!\\)\s|$)</td>
        <td>D:\sarawakjobs\duplicatedemo.notesquare.com_origin\duplicatedemo.notesquare.com_edit\wp-content\uploads_new\company_logos\2021\07\</td>
    </tr>
    <tr>
        <td>([^\\]*.(?:jpg|gif|png|jpeg))</td>
        <td>Test-1-employer.jpg</td>
    </tr>
    

</table>


<table style="width:100%">
    <tr>
        <td colspan="2" align="center"><strong>source</strong></td>
    </tr>
    <tr>
        <td colspan="2">Files Added: admin-custom-forms.php, includes/custom-forms/form-builder.php, includes/custom-forms/form-builder.css, includes/custom-forms/form-builder.js, includes/custom-forms/form-builder-helper.php, includes/custom-forms/gh-button.css, includes/custom-forms/gh-icons.pngnkjnkj</td>
    </tr>
    <tr>
        <th>regex</th>
        <th colspan="2">result</th>
    </tr>
    <tr>
        <td>.*((?<= ).*\.(?:jpg|gif|png|jpeg))</td>
        <td>includes/custom-forms/gh-icons.png</td>
    </tr>
    <tr>
        <td>([^\/]*.(?:jpg|gif|png|jpeg))</td>
        <td>gh-icons.png</td>
    </tr>
    

</table>