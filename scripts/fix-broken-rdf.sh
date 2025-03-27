for file in *.rdf; do
  echo "Processing $file..."
  
  # Use sed to replace xml:lang="anything" with xml:lang="mul"
  sed -i 's/xml:lang="[^"]*"/xml:lang="mul"/g' "$file"
  
  echo "Completed processing $file"
done
