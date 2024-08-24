# Fix opening of too many files
exec { 'Comment out':
  command => 'sed -i "s/15/4096/" /etc/default/nginx; service nginx restart',
  path    => '/usr/bin:/usr/sbin:/bin'
}
