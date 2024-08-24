# Remove user file limits
exec { 'Remove limits':
  command => 'sed -i \'/^holberton/d\' /etc/security/limits.conf',
  path    => '/usr/bin:/usr/sbin:/bin'
}
