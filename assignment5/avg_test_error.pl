$mean = 0;
$data = shift;
$dir=$data;
#$dir=$data;
#print "step 1 ";
=for comment
for(my $i=0; $i<10; $i++){
  system("python nm_fall17.py $dir/$data.data $dir/$data.trainlabels.$i > 
nm_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels nm_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Nearest means error = $mean ($sd)\n";

#q^
$mean = 0;
for(my $i=0; $i<10; $i++){
  system("python3 nb.py $dir/$data.data $dir/$data.trainlabels.$i > 
nb_out.$data");
  $err[$i] = `perl error.pl $dir/$data.labels nb_out.$data`;
  chomp $err[$i];
  print "$err[$i]\n";
  $mean += $err[$i];
 
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "Naive Bayes error = $mean ($sd)\n";
#^if 0;
=cut
#q^
#print "hello ";

$mean = 0;
$total=1;
for(my $i=0; $i<$total; $i++){
  #print(python least_squares_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i  > p_out.$data);
  system("python least_squares_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i  > p_out.$data");
  #print "hello11";
  #$err[$i] = `perl error.py $dir/$data.labels p_out.$data`;
  system("python error.py $dir/$data.labels p_out.$data > error_out.$data");
  #print "hello12";
  
  open my $file, '<', "error_out.$data"; 
  $err[$i] = <$file>;
  print $err[$i];
  chomp $err[$i];
  $mean += $err[$i];
}
$mean /= $total;
$sd = 0;
for(my $j=0; $j<$total; $j++){
  $sd += ($err[$j]-$mean)**2;
}
$sd /= $total;
$sd = sqrt($sd);
print "Perceptron error = $mean ($sd)\n";
#^if 0;

#q^
$mean = 0;
$total=1;
for(my $i=0; $i<$total; $i++){
  system("python hinge_adaptive_eta.py $dir/$data.data $dir/$data.trainlabels.$i > p_out.$data");
  #$err[$i] = `perl error.pl $dir/$data.labels p_out.$data`;
  system("python error.py $dir/$data.labels p_out.$data > error_out.$data");
  #print "hello12";
  
  open my $file, '<', "error_out.$data";
  $err[$i] = <$file>;
  print $err[$i];
  chomp $err[$i];
  $mean += $err[$i];
}
$mean /= $total;
$sd = 0;
for(my $j=0; $j<$total; $j++){
  $sd += ($err[$j]-$mean)**2;
}
$sd /= $total;
$sd = sqrt($sd);
print "Hinge error = $mean ($sd)\n";
#^if 0;
=for comment
q^
$mean = 0;
for(my $i=0; $i<10; $i++){
  ##Create the training data and labels for SVM

  ##Obtain the cross-validated value of C
  $C = `perl cv-svm.pl data_cv labels_cv`;

  ##Predict with that value of C
  system("perl run_svm_light.pl $data.data $data.trainlabels.$i $C");
  $err[$i] = `perl error.pl $data.labels svmpredictions`;
  chomp $err[$i];
  $mean += $err[$i];
}
$mean /= 10;
$sd = 0;
for(my $i=0; $i<10; $i++){
  $sd += ($err[$i]-$mean)**2;
}
$sd /= 10;
$sd = sqrt($sd);
print "SVM error = $mean ($sd)\n";
^if 0;
=cut
