using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System;

public class Capture_position : MonoBehaviour
{

    public GameObject Camera_object;
    public GameObject Marker_object;
    private StreamWriter saveFile;

    // Start is called before the first frame update
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {

        saveFile = new System.IO.StreamWriter("Assets/position_log.txt", append: true);

        string File_name = DateTime.Now.ToString("yyyy-MM-dd hh:mm:ss");

        //Debug.Log(Camera_object.transform.position);



        saveFile.WriteLine(File_name + "/" + Camera_object.transform.position + "/" + Marker_object.transform.position);
        saveFile.Close();

    }
}
